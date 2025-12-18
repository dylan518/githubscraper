package com.spring_movie.service;

import java.io.IOException;
import java.util.ArrayList;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.select.Elements;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.SessionAttribute;
import org.springframework.web.servlet.ModelAndView;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import com.google.gson.Gson;
import com.spring_movie.dao.MovieDao;
import com.spring_movie.dto.MovieDto;
import com.spring_movie.dto.ReservInfoDto;
import com.spring_movie.dto.ReservationDto;
import com.spring_movie.dto.ReviewDto;
import com.spring_movie.dto.ScheduleDto;
import com.spring_movie.dto.TheaterDto;

@Service
public class MovieService {

	@Autowired
	private MovieDao mvdao;
	  
	
	
	//------------------CGV크롤링-----------------------
	public ModelAndView getCgvMovieList() throws IOException {
		System.out.println("MovieService.getCgvMovieList() 호출");
		
		ModelAndView mav = new ModelAndView();
		//next() ::다음 요소를 선택(바로 아랫줄)
				String url = "http://www.cgv.co.kr/movies/?lt=1&ft=0";
				
				//jsoup이 url에 접속하고 그 내용을 doc에 담음.
				Document doc = Jsoup.connect(url).get();
				
				//select () ::괄호안의 선택자로 찾은 요소의 내용을 가져온다는 뜻		
				Elements movieList_div = doc.select("div.sect-movie-chart").eq(0);
				
				//movieList_div가 여러개가 존재하므로, 처음 div에서 ol을 select한다는 뜻
				Elements movieList_ol = movieList_div.select("ol");
				
				
				  ArrayList<MovieDto> cgvMovieList = new ArrayList<MovieDto>();
				  MovieDto cgvMovie;
				  
				  int insertCount = 0;

				
				for (int i =0; i<movieList_ol.size(); i++) {
					for(int j=0; j<movieList_ol.eq(i).select("li").size(); j++) {
						cgvMovie = new MovieDto(); 
					
						String detailurl="http://www.cgv.co.kr"+movieList_ol.eq(i).select("li").eq(j).select("div.box-contents a").attr("href");		
						Document detailDoc = Jsoup.connect(detailurl).get();
						Elements baseMovie = detailDoc.select("div.sect-base-movie");	
						
						//영화이름
						String movieName =baseMovie.select("div.sect-base-movie div.box-contents div.title strong").text();
						cgvMovie.setMvname(movieName);
						//감독
						String moviePd =baseMovie.select("div.sect-base-movie div.box-contents div.spec dd").eq(0).text();
						cgvMovie.setMvpd(moviePd);
						//배우
						String movieActor =baseMovie.select("div.sect-base-movie div.box-contents div.spec dd.on").eq(0).text();
						cgvMovie.setMvactor(movieActor);
						//장르
						String movieGenre =baseMovie.select("div.sect-base-movie div.box-contents div.spec dd.on").eq(0).next().text().replaceAll("장르 :", "");
						cgvMovie.setMvgenre(movieGenre);
						
						//여기서 바로 나누어 줄 수 있음. baseMovie.select("div.sect-base-movie div.box-contents div.spec dd.on").eq(1).text().split(", ")[0]; 그리고...[1];
						String movieTimeAge =baseMovie.select("div.sect-base-movie div.box-contents div.spec dd.on").eq(1).text();
						//연령가
						
						String moviePoster =baseMovie.select("div.sect-base-movie div.box-image img").eq(0).attr("src");
						//포스터 이미지 이름
						cgvMovie.setMvposter(moviePoster);
						
						String Age = movieTimeAge.split(", ")[0];
						cgvMovie.setMvage(Age);
						String TimeStr =  movieTimeAge.split(", ")[1];
						
						TimeStr=TimeStr.replaceAll(",", "");
					
						cgvMovie.setMvtime(TimeStr);						
						//시간						
						
						//개봉일
						String movieOpen =baseMovie.select("div.sect-base-movie div.box-contents div.spec dd.on").eq(2).text();
						cgvMovie.setMvopen(movieOpen);
						System.out.println(cgvMovie);
						
						cgvMovieList.add(cgvMovie);
						
						
						
					//지정해서 찾아주는게 일이넹.. 
						//찾을때 필요한 split(",")[i], next(), replace("?","")... 	
					}
				}
				for(int i =0; i<cgvMovieList.size(); i++) {
					
					//mvname,mvopen 으로 select하여 중복 없으면 실행되도록
					String mvnameCheck = cgvMovieList.get(i).getMvname();
					String mvopenCheck = cgvMovieList.get(i).getMvopen();
					
					System.out.println("영화이름,개봉일로 기존영화목록에서 해당영화 검색");
					int searchCount = mvdao.mvSearch(mvnameCheck,mvopenCheck);
					String mvcode= "";
					if(searchCount==0) {
						//1영화코드 생성 (select)
						
						String maxMvCode = mvdao.maxMvCode();
						System.out.println("최근 영화코드: "+maxMvCode);
						if(maxMvCode == null ) {
							mvcode= "MV001";
						}else {
							int maxMvNum = Integer.parseInt(maxMvCode.replace("MV", ""))+1;
							System.out.println("maxMvNum : "+maxMvNum);
							if(maxMvNum<10) {
								mvcode = "MV00"+maxMvNum;
							}else if(maxMvNum<100) {
								mvcode = "MV0"+maxMvNum;
								
							}else {
								mvcode = "MV"+maxMvNum;
							}
							
						}
						//2영화정보 insert
						System.out.println("최종 mvcode :"+mvcode);
						cgvMovieList.get(i).setMvcode(mvcode);
					
							int insertResult = mvdao.insertMovie(cgvMovieList.get(i));
							if(insertResult ==1) {
								insertCount +=1;
							}												
					}else {
						System.out.println("이미 등록된 영화입니다.");
					}
										
				}
				System.out.println("총 "+insertCount+"개의 영화가 등록되었습니다");
				
		mav.setViewName("redirect:/");
		return mav;
	}
	
	
	
	
	//------------------영화목록 페이지-----------------------

	public ModelAndView MovieList() {
		System.out.println("MovieService.movieList() 호출");
		ModelAndView  mav= new ModelAndView();
		MovieDto mvContents ;
		//영화목록 조회
		ArrayList<MovieDto> mvList =  mvdao.selectMovieList();
		System.out.println(mvList);
		for(int i = 0; i<mvList.size(); i++) {
			mvContents=mvdao.getthumb(mvList.get(i).getMvcode());
			int thup = mvContents.getThumbsup();
			int thdown = mvContents.getThumbsdown();
			
			mvList.get(i).setThumbsup(thup);
			mvList.get(i).setThumbsdown(thdown);
			
			double reRate = mvdao.getreRate(mvList.get(i).getMvcode());
			mvList.get(i).setReRate(reRate);
		}
		
		mav.addObject("mvList",mvList);
		mav.setViewName("movie/MovieList");
		return mav;
	}




	public ModelAndView MovieView(String mvcode) {
		System.out.println("MovieView서비스 이동뒤 호출");
		ModelAndView  mav= new ModelAndView();
		System.out.println("mvcode:"+mvcode);
		MovieDto mvContents = new MovieDto();
		mvContents = mvdao.mvView(mvcode);
		System.out.println(mvContents);
		
		MovieDto mvContents2 = mvdao.getthumb(mvcode);
		int thup = mvContents2.getThumbsup();
		int thdown = mvContents2.getThumbsdown();
		
		mvContents.setThumbsup(thup);
		mvContents.setThumbsdown(thdown);
		
		ArrayList<ReviewDto> reviewList = mvdao.getrvList(mvcode);
		
		double reRate = mvdao.getreRate(mvcode);
		mvContents.setReRate(reRate);
		
		
		System.out.println(mvcode+"의 관람평 개수:"+reviewList.size());
		System.out.println(mvContents);
		
		mav.addObject("reviewList",reviewList);
		mav.addObject("mvContents",mvContents);
		
		mav.setViewName("movie/MovieView");
		return mav;
	}




	public ModelAndView movieReservationPage() {
		System.out.println("movieReservationPage서비스 이동뒤 호출");
		ModelAndView  mav= new ModelAndView();
		
		
		//1.영화목록 조회(예매가능한 영화: 스케쥴에있는 영화만)
		ArrayList<MovieDto> reMvList = mvdao.slelctReserveMvList();
		System.out.println(reMvList);
		
		
		mav.addObject("reMvList",reMvList);
		mav.setViewName("movie/MovieReservationPage");
		return mav;
	}




	public String getThList(String mvcode) {
		Gson gson = new Gson();
		ArrayList<TheaterDto> thList = mvdao.getThList(mvcode);
		String thList_json = gson.toJson(thList);
		return thList_json;
	}




	public String getCsDateList(String mvcode, String thcode) {
		Gson gson = new Gson();
		String csDateList_json="";
		ArrayList<ScheduleDto> thList = mvdao.getCsDateList(mvcode,thcode);
		for(int i =0; i<thList.size(); i++) {
			thList.get(i).setScdate_after(thList.get(i).getScdate().replaceFirst("-", "년")); 
			thList.get(i).setScdate_after(thList.get(i).getScdate_after().replaceFirst("-", "월")); 
			thList.get(i).setScdate_after(thList.get(i).getScdate_after()+"일"); 			
		}
		csDateList_json = gson.toJson(thList);
		return csDateList_json;
	}




	public String getScRoomTimeList(String mvcode, String thcode, String scdate) {
		Gson gson = new Gson();
		String csRoomTimeList_json="";
		ArrayList<ScheduleDto> csRoomTimeList = mvdao.getScRoomTimeList(mvcode,thcode,scdate);
		csRoomTimeList_json = gson.toJson(csRoomTimeList);
		return csRoomTimeList_json;
	}




	public ModelAndView insertReservation(ReservationDto rdto, RedirectAttributes ra) {
		ModelAndView  mav= new ModelAndView();
		String Recode="";
		String getRecode=mvdao.getReservationRecode();
		System.out.println("가져온 recode값:"+getRecode);
		if(getRecode == null) {
			Recode= "RE001";
		}else {
			int getReNum = Integer.parseInt(getRecode.substring(2))+1;
			if (getReNum<10) {
				Recode="RE00"+getReNum;
			}else if(getReNum<100) {
				Recode="RE0"+getReNum;
			}else if(getReNum<1000) {
				Recode="RE"+getReNum;
			}
		}
		rdto.setRecode(Recode);
		System.out.println("코드 : "+Recode+"날짜 및 시간:"+rdto.getRescdate()+":");
		int insertResult =0;
		
		
		try {
			 insertResult=mvdao.insertReservation(rdto);
			
		} catch (Exception e) {
			// TODO: handle exception
		}
		if (insertResult>0) {		
			System.out.println("입력성공");
			ReservInfoDto reDto = mvdao.selectReservation2(Recode);
			ra.addFlashAttribute("reservInfoflash",reDto);
			mav.setViewName("redirect:/");
		}
		
		return mav;
	}




	public ModelAndView movieReservationInfoPage(String mid,RedirectAttributes ra) {
		System.out.println("예매내역 요청 Service");
		ModelAndView  mav= new ModelAndView();
		if(mid==null) {
			String loginMsg = "로그인 후 이용해주세요";
			ra.addFlashAttribute("loginMsg",loginMsg);
			mav.setViewName("redirect:/memberLoginForm");
		}else {
			ArrayList<ReservInfoDto> rdtoList = new ArrayList<ReservInfoDto>();
			
			rdtoList=mvdao.selectReservation(mid);
			
			
			
			for (int i = 0; i<rdtoList.size(); i++) {
				String revinforecode = rdtoList.get(i).getRecode();
				ReviewDto reviewDto = mvdao.getreviewcheck(revinforecode);	
				if (reviewDto == null) {
					rdtoList.get(i).setCheckRv(0);
				}else{					
					rdtoList.get(i).setCheckRv(1);
				}
				
			}
			
			
			mav.addObject("rdtoList",rdtoList);
			System.out.println("예매한목록:"+rdtoList);
			mav.setViewName("movie/MovieReservationInfo");
		}				
		return mav;
	}




	public ModelAndView deleteReserv(String recode,RedirectAttributes ra) {
		ModelAndView mav =new ModelAndView();
		int deleteResult=mvdao.deleteReserv(recode);
		if(deleteResult>0) {
			String reInfoMsg = "예약취소 되었습니다";
			ra.addFlashAttribute("reInfoMsg",reInfoMsg);
			mav.setViewName("redirect:/movieReservationInfoPage");
		}
		return mav;
	}




	public ModelAndView insertReview(ReviewDto review, RedirectAttributes ra) {
		
		ModelAndView mav =new ModelAndView();
		int insertrvResult = mvdao.insertReview(review);
		if(insertrvResult>0) {
					
			String reInfoMsg="관람평이 작성되었습니다.";
			ra.addFlashAttribute("reInfoMsg",reInfoMsg);
			mav.setViewName("redirect:/movieReservationInfoPage");
			
		}
		return mav;
	}




	public String getcomentInfo(String recode) {
		
		ReviewDto reservInfo=mvdao.getcomentInfo(recode);
		System.out.println(reservInfo);
		Gson gson = new Gson();
		String result = gson.toJson(reservInfo);
		return result;
	}




	public ModelAndView updateReview(ReviewDto modiReview,RedirectAttributes ra,int checkView){
		ModelAndView mav =new ModelAndView();
		int updateResult=mvdao.updateReview(modiReview);
		if(updateResult>0) {
			if (checkView == 1) {
				String reInfoMsg="관람평 수정이 완료되었습니다";
				ra.addFlashAttribute("reInfoMsg",reInfoMsg);
				mav.addObject("mvcode",modiReview.getRvmvcode());
				mav.setViewName("redirect:/movieView");	
			}else {
				
				String reInfoMsg="관람평 수정이 완료되었습니다";
				ra.addFlashAttribute("reInfoMsg",reInfoMsg);
				mav.setViewName("redirect:/movieReservationInfoPage");	
			}
			
		}
		return mav;
	}




	public ModelAndView getSearchMovieList(String inputWord) {
		ModelAndView mav =new ModelAndView();
		
		ArrayList<MovieDto> resultMvList = mvdao.getSearchMovieList(inputWord);
		ArrayList<MovieDto> resultMvListSC = mvdao.getSearchMovieListSC(inputWord);
		
		mav.addObject("resultMvList",resultMvList);
		mav.addObject("resultMvListSC",resultMvListSC);
		mav.setViewName("movie/MovieSearchResult");
		return mav;
	}




	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
}
